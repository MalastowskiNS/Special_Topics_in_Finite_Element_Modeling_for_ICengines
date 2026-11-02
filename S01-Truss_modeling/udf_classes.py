import numpy as np                                   # библиотека с математическими операциями    
import matplotlib.pyplot as plt                      # библиотека для отображения графиков
from dataclasses import dataclass                    # библиотека для создания класса узла, стержня



@dataclass
class Node:
    id: int
    x: float
    y: float
    fx: float = 0.0
    fy: float = 0.0
    fix_x: bool = False
    fix_y: bool = False


@dataclass
class Bar:
    id: int
    n1: int
    n2: int
    E: float
    A: float



class Truss:
    def __init__(self):
        self.nodes = {}
        self.bars = []

    def add_node(self, node: Node):
        self.nodes[node.id] = node

    def add_bar(self, bar: Bar):
        self.bars.append(bar)

    def build_index(self):
        self.node_ids = sorted(self.nodes.keys())
        self.id_to_index = {nid: i for i, nid in enumerate(self.node_ids)}

    def node_dofs(self, node_id):
        i = self.id_to_index[node_id]
        return [2 * i, 2 * i + 1]

    def bar_geometry(self, bar: Bar):
        n1 = self.nodes[bar.n1]
        n2 = self.nodes[bar.n2]
        dx = n2.x - n1.x
        dy = n2.y - n1.y
        L = (dx**2 + dy**2) ** 0.5
        c = dx / L
        s = dy / L
        return dx, dy, L, c, s

    def bar_stiffness(self, bar: Bar):
        _, _, L, c, s = self.bar_geometry(bar)
        k = bar.E * bar.A / L
        return k * np.array([
            [ c*c,  c*s, -c*c, -c*s],
            [ c*s,  s*s, -c*s, -s*s],
            [-c*c, -c*s,  c*c,  c*s],
            [-c*s, -s*s,  c*s,  s*s]
        ])

    def assemble_K(self):
        self.build_index()
        ndof = 2 * len(self.nodes)
        K = np.zeros((ndof, ndof))

        for bar in self.bars:
            ke = self.bar_stiffness(bar)
            dofs = self.node_dofs(bar.n1) + self.node_dofs(bar.n2)
            K[np.ix_(dofs, dofs)] += ke

        return K

    def assemble_F(self):
        ndof = 2 * len(self.nodes)
        F = np.zeros(ndof)

        for nid in self.node_ids:
            node = self.nodes[nid]
            ux, uy = self.node_dofs(nid)
            F[ux] = node.fx
            F[uy] = node.fy

        return F

    def get_fixed_free_dofs(self):
        fixed = []
        free = []

        for nid in self.node_ids:
            node = self.nodes[nid]
            ux, uy = self.node_dofs(nid)

            if node.fix_x:
                fixed.append(ux)
            else:
                free.append(ux)

            if node.fix_y:
                fixed.append(uy)
            else:
                free.append(uy)

        return fixed, free

    def solve(self):
        K = self.assemble_K()
        F = self.assemble_F()
        fixed, free = self.get_fixed_free_dofs()

        K_ff = K[np.ix_(free, free)]
        F_f = F[free]

        u = np.zeros(len(F))
        u[free] = np.linalg.solve(K_ff, F_f)

        R = K @ u - F

        return {
            "K": K,
            "F": F,
            "u": u,
            "R": R,
            "free": free,
            "fixed": fixed,
            "K_ff": K_ff,
            "F_f": F_f,
        }
    def bar_axial_force(self, bar: Bar, u_global):
        _, _, L, c, s = self.bar_geometry(bar)
        dofs = self.node_dofs(bar.n1) + self.node_dofs(bar.n2)
        u_e = u_global[dofs]
        delta_L = np.array([-c, -s, c, s]) @ u_e
        N = bar.E * bar.A / L * delta_L
        return N
    def bar_stress(self, bar: Bar, u_global):
        N = self.bar_axial_force(bar, u_global)
        return N / bar.A
    def plot_deformed(self, u=None, scale="auto", show_node_ids=True, figsize=(7, 5)):
        """
        Рисует исходную и деформированную ферму.

        Параметры
        ---------
        u : np.ndarray or None
            Полный вектор перемещений.
            Если None, рисуется только исходная схема.
        scale : float or "auto"
            Масштаб деформаций.
            Если "auto", масштаб подбирается автоматически.
        show_node_ids : bool
            Подписывать ли номера узлов.
        figsize : tuple
            Размер рисунка.
        """
        self.build_index()

        # исходные координаты узлов
        x0 = {}
        y0 = {}
        for nid in self.node_ids:
            node = self.nodes[nid]
            x0[nid] = node.x
            y0[nid] = node.y

        # если решения нет — только исходная схема
        if u is None:
            scale_value = 1.0
            xd = x0.copy()
            yd = y0.copy()
        else:
            # деформированные координаты
            xd = {}
            yd = {}

            # характерный размер конструкции
            xs = np.array([x0[nid] for nid in self.node_ids])
            ys = np.array([y0[nid] for nid in self.node_ids])
            size_ref = max(xs.max() - xs.min(), ys.max() - ys.min(), 1.0)

            # максимальное перемещение
            max_disp = 0.0
            for nid in self.node_ids:
                ux, uy = self.node_dofs(nid)
                disp = (u[ux]**2 + u[uy]**2) ** 0.5
                max_disp = max(max_disp, disp)

            if scale == "auto":
                if max_disp < 1e-14:
                    scale_value = 1.0
                else:
                    scale_value = 0.15 * size_ref / max_disp
            else:
                scale_value = float(scale)

            for nid in self.node_ids:
                ux, uy = self.node_dofs(nid)
                xd[nid] = x0[nid] + scale_value * u[ux]
                yd[nid] = y0[nid] + scale_value * u[uy]

        fig, ax = plt.subplots(figsize=figsize)

        # исходная схема
        for bar in self.bars:
            n1, n2 = bar.n1, bar.n2
            ax.plot(
                [x0[n1], x0[n2]],
                [y0[n1], y0[n2]],
                "-",
                color="black",
                linewidth=1.5,
                label="Исходная схема" if bar.id == self.bars[0].id else None
            )

        # деформированная схема
        if u is not None:
            for bar in self.bars:
                n1, n2 = bar.n1, bar.n2
                ax.plot(
                    [xd[n1], xd[n2]],
                    [yd[n1], yd[n2]],
                    "--",
                    color="black",
                    linewidth=2.5,
                    label="Деформированная схема" if bar.id == self.bars[0].id else None
                )

        # узлы
        ax.scatter(
            [x0[nid] for nid in self.node_ids],
            [y0[nid] for nid in self.node_ids],
            s=40,
            color="black",
            zorder=3
        )

        if u is not None:
            ax.scatter(
                [xd[nid] for nid in self.node_ids],
                [yd[nid] for nid in self.node_ids],
                s=40,
                color="black",
                zorder=3
            )

        # подписи узлов
        if show_node_ids:
            for nid in self.node_ids:
                ax.text(x0[nid], y0[nid], f" {nid}", fontsize=11)
                if u is not None:
                    ax.text(xd[nid], yd[nid], f" {nid}'", fontsize=11)

        title = "Исходная и деформированная схема"
        if u is not None:
            title += f" (масштаб деформаций = {scale_value:.2f})"

        ax.set_title(title)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.axis("equal")
        ax.grid(True, alpha=0.3)
        ax.legend()
        plt.show()
from .geom import geom


class geom_violin(geom):
    DEFAULT_AES = {'y': None, 'color': 'black'}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'identity'}

    def plot(self, ax, data, _aes, x_levels):
        params = self._get_plot_args(data, _aes)
        x_levels = sorted(x_levels)
        variables = _aes.data

        xticks = []
        for (i, xvalue) in enumerate(x_levels):
            subset = data[data[variables['x']]==xvalue]
            yi = subset[variables['y']].values

            # so this is weird, apparently violinplot is *the only plot that
            # you can't set the color, shape, etc. as an argument. i know, it
            # makes no sense (http://stackoverflow.com/questions/26291479/changing-the-color-of-matplotlibs-violin-plots)
            plot_parts = ax.violinplot(yi, positions=[i], showextrema=False)
            for pc in plot_parts['bodies']:
                # TODO: make this pull from params
                pc.set_facecolor('white')
                pc.set_edgecolor('black')
                pc.set_alpha(1.0)
                pc.set_linewidth(1.0)

            xticks.append(i)

        ax.set_xticks(xticks)
        ax.set_xticklabels(x_levels)

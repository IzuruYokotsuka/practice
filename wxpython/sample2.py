import numpy as np
import pandas as pd

import wx
import wx.grid

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'


class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None, hoge=[]):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.hoge = hoge
        if data is None:
            data = pd.DataFrame()
        self.data = data

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data.columns) + 1

    def GetValue(self, row, col):
        if col == 0:
            return self.data.index[row]
        return self.data.iloc[row, col - 1]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col - 1] = value

    def GetColLabelValue(self, col):
        if col == 0:
            if self.data.index.name is None:
                return 'Index'
            else:
                return self.data.index.name
        return str(self.data.columns[col - 1])

    def GetTypeName(self, row, col):
        return wx.grid.GRID_VALUE_STRING

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        x = [row, col]
        if x in self.hoge:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr


class MyFrame(wx.Frame):
    """
    Frame that holds all other widgets
    """

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY, "Pandas")
        self._init_gui()
        self.Layout()
        self.Show()

    def _init_gui(self):
        df = pd.DataFrame(np.random.random((10, 5)))
        # 色を塗りたいところ
        x = [[1,1], [3,3], [5,5]]
        table = DataTable(df, x)

        grid = wx.grid.Grid(self, -1)
        grid.SetTable(table, takeOwnership=True)
        grid.AutoSizeColumns()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.exit)

    def exit(self, event):
        self.Destroy()


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

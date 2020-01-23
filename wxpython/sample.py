import wx
import wx.grid


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Title", size=(450,200))
        self.InitializeComponents()

    def InitializeComponents(self):
        grid = wx.grid.Grid(self)
        grid.CreateGrid(5, 2)

        # Set column labels.
        grid.SetColLabelValue(0, "Title")
        grid.SetColLabelValue(1, "URL")

        # Set cell values.
        grid.SetCellValue(0, 0, "Google")
        grid.SetCellValue(0, 1, "http://google.com/")
        grid.SetCellValue(1, 0, "Yahoo! JAPAN")
        grid.SetCellValue(1, 1, "http://www.yahoo.co.jp/")
        grid.SetCellValue(2, 0, "Python")
        grid.SetCellValue(2, 1, "http://www.python.org/")
        grid.SetCellValue(3, 0, "Python Documentation")
        grid.SetCellValue(3, 1, "http://docs.python.org/")
        grid.SetCellValue(4, 0, "wxPython")
        grid.SetCellValue(4, 1, "http://www.wxpython.org/")

        # Alignment.
        grid.AutoSize()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    MyFrame().Show(True)
    app.MainLoop()

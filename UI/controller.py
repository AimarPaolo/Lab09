import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.set_coll = set()

    def handleAnalizza(self, e):
        self._view._txt_result.controls.clear()
        distanza_minima = self._view._txtIn.value
        if distanza_minima == "":
            self._view.create_alert("Inserire una distanza minima!!!")
            self._view.update_page()
            return
        try:
            int(distanza_minima)
        except ValueError:
            self._view.create_alert("Inserire una distanza minima in formato di numero!!!")
            self._view.update_page()
            return
        self._set_coll = self._model.buildGraph(distanza_minima)
        self._view._txt_result.controls.append(ft.Text(f"valore inserito {distanza_minima}"))
        nNode = self._model.getNumNodes()
        nEdges = self._model.getNumEdges()
        self._view._txt_result.controls.append(ft.Text(f"è stato creato il grafo"))
        self._view._txt_result.controls.append(ft.Text(f"Il numero di nodi è: {nNode} mentre il numero degli archi è: {nEdges}"))
        for i in self._set_coll:
            self._view._txt_result.controls.append(ft.Text(i))
        self._view.update_page()


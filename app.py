from multiapp import MultiApp
import modeler
import preprocessor

app = MultiApp()

app.add_app("Preprocessing", preprocessor.app)
app.add_app("Modelling", modeler.app)

app.run()


#MultiApp classından gelen bilgi ile sistemin başlatılması ve sayfa geçişlerinde işlem görmektedir.


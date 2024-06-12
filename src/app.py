
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd


# Criando o aplicativo Dash
app = dash.Dash(__name__)

server = app.server

# Carregando dados de exemplo 
# (pode ser substituído pelos seus próprios dados)
df = pd.read_csv('src\predictive_maintenance.csv')



app.layout = html.Div(children=[
    html.H1(children='Dashboard interativo de manutenção preventiva', style={'color':'blue', 'text-align': 'center'}),
    dcc.Graph(
        id='plot',
        figure=px.bar(df, barmode = 'group', x='Type', y='Failure Type', color = 'Failure Type',
                          title='Defeitos por tamanho de máquina'
                          )
 
    ),
    html.H2(children='Gráfico de Pizza', style={'color':'Red', 'text-align': 'center'}),
    dcc.Graph(
            id = 'plt',
            figure=px.pie(df, values="Target", names="Failure Type", title='Falhas mais comuns em todas as máquinas')
        
    )

]
)




# Executando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
   

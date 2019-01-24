import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import pickle

df = pd.read_csv('data/train.csv', index_col = 0)

plot_x1y = go.Scatter(x = df['x1'], y = df['y'], mode = 'markers', name = 'x1 / y')
plot_x2y = go.Scatter(x = df['x2'], y = df['y'], mode = 'markers', name = 'x2 / y')
plot_x1x2 = go.Scatter(x = df['x1'], y = df['x2'], mode = 'markers', name = 'x1 / x2')

graph_x1x2 = dcc.Graph(
        id = 'scatter_plot_x1_x2',
        figure = go.Figure(
            data = [plot_x1x2],
            layout = go.Layout(
                autosize = False,
                width = 500,
                height = 500,
                xaxis = {
                    'title': 'x1',
                    'ticklen': 5,
                    'gridwidth': 2,
                },
                yaxis = {
                    'title': 'x2',
                    'ticklen': 5,
                    'gridwidth': 2,
                },
                margin = go.layout.Margin(
                    l = 50,
                    r = 50,
                    b = 50,
                    t = 50,
                    pad = 4
                ),
            )
        )
    )

graph_x1y = dcc.Graph(
        id = 'scatter_plot_x1_y',
        figure = go.Figure(
            data = [plot_x1y],
            layout = go.Layout(
                autosize = False,
                width = 500,
                height = 500,
                xaxis = {
                    'title': 'x1',
                    'ticklen': 5,
                    'gridwidth': 2,
                },
                yaxis = {
                    'title': 'y1',
                    'ticklen': 5,
                    'gridwidth': 2,
                },
                margin = go.layout.Margin(
                    l = 50,
                    r = 50,
                    b = 50,
                    t = 50,
                    pad = 4
                ),
                #paper_bgcolor = '#7f7f7f',
                #plot_bgcolor = '#c7c7c7'
            )
        )
    )
                
graph_x2y = dcc.Graph(
        id = 'scatter_plot_x2_y',
        figure = go.Figure(
            data = [plot_x2y],
            layout = go.Layout(
                autosize = False,
                width = 500,
                height = 500,
                xaxis = {
                    'title': 'x2',
                    'ticklen': 5,
                    'gridwidth': 2,
                },
                yaxis = {
                    'title': 'y',
                    'ticklen': 5,
                    'gridwidth': 2,
                },
                margin = go.layout.Margin(
                    l = 50,
                    r = 50,
                    b = 50,
                    t = 50,
                    pad = 4
                ),
            )
        )
    )
                


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Train data'),

    html.Div([
        html.Div([
            html.H3('X1 / X2'),
            graph_x1x2
        ], className="four columns"),

        html.Div([
            html.H3('X1 / Y'),
            graph_x1y
        ], className="four columns"),

        html.Div([
            html.H3('X2 / Y'),
            graph_x2y
        ], className = "four columns"),
    ], className = "row"),
    
 
    html.Div([
        dcc.Input(id = 'input-box x1', placeholder = 'Enter x1..', type = 'double', value = 0.1),
        dcc.Input(id = 'input-box x2', placeholder = 'Enter x2..', type = 'double', value = 0.2),
        html.Div(id = 'output-keypress')
    ]),
])
    

@app.callback(dash.dependencies.Output('output-keypress', 'children'),
              [dash.dependencies.Input('input-box x1', 'value'),
               dash.dependencies.Input('input-box x2', 'value')])

def update_output(input1, input2):
    filename = 'data/nusvm_model.sav'
    model = pickle.load(open(filename, 'rb'))
    X_test = pd.DataFrame({
        'x1': [input1],
        'x2': [input2]
        })
    a = model.predict(X_test)
    return 'The predicted value is {}'.format(a[0])
    
    


if __name__ == '__main__':
    app.run_server(debug = True)
    
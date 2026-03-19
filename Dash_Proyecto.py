import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import ConsultasPython as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Mostrar el nombre del sector y el nombre de la empresa dentro del S&P y agruparlas por el nombre del sector. 
con_1 = Connection()
con_1.openConnection()
query_1 = pd.read_sql_query(sql.Sect_SP(), con_1.connection)
con_1.closeConnection()
dfSector_1 = pd.DataFrame(query_1, columns=["sector", "s_p_name"])

# Grafico barras
figBarSector_1 = px.bar(dfSector_1.head(20), x="sector", y="s_p_name",
                      height=1000,
                      title='Barras Horizontales')
# Grafico barras horizontales
figBarSector_1H = px.bar(dfSector_1.head(30),  x="sector", y="s_p_name", 
                      orientation = 'h',
                      height=1000,
                      title='Barras Verticales')
#Grafico pie
figPieSector_1 = px.pie(dfSector_1.head(20), names="sector", values="s_p_name")
#Grafico linea
figLineSector_1 = px.line(dfSector_1.head(20),  x="sector", y="s_p_name")
#Mapa
figMapSector_1 = px.choropleth(dfSector_1, locations="sector",
                            locationmode="sector names",
                            color="s_p_name", 
                            hover_name="sector", 
                            color_continuous_scale=["#99ccff", "#ff3333"])

# Layout 
app.layout = html.Div(children=[
    html.H1(children='Dashboard'), # genera <h1>Dashboard</h1>
    html.Div(className= "container", children=[
        # Row for cases
        html.Div(className= "row", children=[
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H2(children='Sector and S&P'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barSector',
                                    figure=figBarSector_1
                                ),    
                    ]),    
                    
                ]),
            ]),
            # Col for horizontal bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H2(children='Sector and S&P'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barHSector',
                                    figure=figBarSector_1H
                                ),   
                    ]),    
                    
                ]),
            ]),
            
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H2(children='Sector and S&P'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieSector',
                                    figure=figPieSector_1
                                ), 
                    ]),    
                    
                ]),
            ]),
            
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H2(children='Sector and S&P'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='lineSector',
                                      figure=figLineSector_1
                                  ),
                    ]),    
                    
                ]),
            ]),
        ]),
    ]),
    html.H2(children='Sector and S&P'),
    dcc.Graph(
        id='mapCasesByCountry',
        figure=figMapSector_1
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Ana', 'Pedro', 'Luis'],
    'Edad': [23, 34, 29],
    'Salario': [5000, 6000, 7000]
}
df = pd.DataFrame(data)

# Inicializa la aplicación Dash
app = Dash(__name__)
server = app.server

# Define los estilos
titulo_style = {
    'textAlign': 'center',
    'color': 'blue'
}

footer_style = {
    'textAlign': 'center',
    'padding': '10px',
    'marginTop': '20px',
    'backgroundColor': '#f1f1f1'
}

# Diseño de la aplicación
app.layout = html.Div([
    # Título principal
    html.H1("Distribuidora Lugor S.A.S", style=titulo_style),
    # Parrafo
    html.P("Aplicación Web dinámica para el análisis de información"),
    # Gráficos
    html.Div([
        dcc.Graph(
            id='grafico-barras',
            figure=px.bar(df, x='Nombre', y='Salario', color='Nombre', title="Salarios por Persona"),
            style={'width': '50%'}
        ),
        dcc.Graph(
            id='grafico-torta',
            figure=px.pie(df, names='Nombre', values='Salario', title="Distribución de Salarios por Persona"),
            style={'width': '50%'}
        )
    ], style={'display': 'flex', 'justify-content': 'space-around', 'width': '100%'}),
    # Pie de página
    html.Footer(
        [
            "© Todos los derechos reservados",
            html.Br(),  # Salto de línea
            "Dirección 24#45"
        ],
        style=footer_style
    )
], lang='es')  # Establecer idioma en español

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)




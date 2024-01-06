import base64
import os
from io import BytesIO
from statistics import mean, median, variance
import matplotlib.pyplot as plt

from dotenv import load_dotenv

from app.utils.utils_format import (
    get_berry_growth_times,
    get_ids_by_berry_url,
    get_names,
    get_paginated_data
)

load_dotenv()


class Berries:
    def __init__(self) -> None:
        self.base_api_url = os.getenv("POKEAPI_BASE_URL", "https://pokeapi.co/api/v2")
    
    def get_berries_stats(self):
        """_summary_

        Raises:
            HTTPException: _description_

        Returns:
            data: {
                "berries_names": [...],
                "min_growth_time": "" // time, int
                "median_growth_time": "", // time, float
                "max_growth_time": "" // time, int
                "variance_growth_time": "" // time, float
                "mean_growth_time": "", // time, float
                "frequency_growth_time": "", // time, {growth_time: frequency, ...}

            }
        """
        response = {}

        berry_url = self.base_api_url + "/berry/"

        berry_data = get_paginated_data(berry_url)
        berries_names = sorted(get_names(berry_data))
        berry_ids = get_ids_by_berry_url(berry_data)
        berry_growth_times = sorted(get_berry_growth_times(berry_url, berry_ids))

        response = {
            "berries_names": berries_names,
            "min_growth_time": self.min_growth_time(berry_growth_times),
            "median_growth_time": self.median_growth_time(berry_growth_times),
            "max_growth_time": self.max_growth_time(berry_growth_times),
            "variance_growth_time": self.variance_growth_time(berry_growth_times),
            "mean_growth_time": self.mean_growth_time(berry_growth_times),
            "frequency_growth_time": self.frequency_growth_time(berry_growth_times)
        }
        self.generate_histogram(berry_growth_times)
        return response
    

    def min_growth_time(self, growth_times: list):
        return int(min(growth_times))


    def median_growth_time(self, growth_times: list):
        return round(float(median(growth_times)), 2)

    def max_growth_time(self, growth_times: list):
        return max(growth_times)

    def variance_growth_time(self, growth_times: list):
        return round(float(variance(growth_times)), 2)

    def mean_growth_time(self, growth_times: list):
        return round(float(mean(growth_times)), 2)

    def frequency_growth_time(self, growth_times: list):
        frequency_growth_time = {}
        for time in growth_times:
            frequency_growth_time[time] = frequency_growth_time.get(time, 0) + 1
        return frequency_growth_time

    def generate_histogram(self, growth_times: list):
        min_data = self.min_growth_time(growth_times)
        max_data = self.max_growth_time(growth_times)
        # Crear un histograma
        plt.hist(growth_times, bins=range(min_data, max_data + 1), align='left', alpha=0.7, edgecolor='black')

        # Configurar etiquetas y título
        plt.xlabel('Value')
        plt.ylabel('Frecuency')
        plt.title('Growth time histogram')

        # Guardar la figura en un BytesIO
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        # Convertir la figura a base64
        imagen_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        # Crear el HTML con la imagen incrustada
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Growth time histogram</title>
        </head>
        <body>
            <h1>Poke Api Stats</h1>
            <img src="data:image/png;base64, {imagen_base64}" alt="Histogram">
        </body>
        </html>
        """

        # Guardar el HTML en un archivo
        with open('histogram.html', 'w') as archivo_html:
            archivo_html.write(html)
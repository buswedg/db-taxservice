import os
import time

import pandas as pd
from django.core.management import BaseCommand
from tqdm import tqdm

from apps.tax.models import TaxRate


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-d', '--data_folder', type=str, required=True)

    def handle(self, *args, **options):
        cols = {
            'State': str,
            'ZipCode': str,
            'TaxRegionName': str,
            'EstimatedCombinedRate': float,
            'StateRate': float,
            'EstimatedCountyRate': float,
            'EstimatedCityRate': float,
            'EstimatedSpecialRate': float,
            'RiskLevel': int
        }

        def rebuild_tax(**kwargs):
            for filename in os.listdir(kwargs['data_folder']):
                if filename.endswith('.csv'):

                    filepath = os.path.join(kwargs['data_folder'], filename)
                    df = pd.read_csv(filepath, dtype=cols)
                    for item in tqdm(df.to_dict('records'), desc=f'Processing {filename}', total=len(df)):
                        fields = {
                            'estimated_combined_rate': item['EstimatedCombinedRate'],
                            'state_rate': item['StateRate'],
                            'estimated_county_rate': item['EstimatedCountyRate'],
                            'estimated_city_rate': item['EstimatedCityRate'],
                            'estimated_special_rate': item['EstimatedSpecialRate'],
                            'risk_level': item['RiskLevel']
                        }

                        TaxRate.objects.update_or_create(
                            state=item['State'],
                            zipcode=item['ZipCode'],
                            tax_region_name=item['TaxRegionName'],
                            defaults=fields
                        )

        ################################################################
        start_time = time.time()
        print("rebuild_tax({})".format(options))

        rebuild_tax(data_folder=options['data_folder'])

        end_time = time.time() - start_time
        print("completed in {}".format(end_time))

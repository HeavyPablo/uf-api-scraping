from flask import request, jsonify

from app.scrapers import UfScraper
from app.utils.validation import Validation


class UfController:

    def __init__(self):
        self.validator = Validation()

    def index(self):
        date = request.args.get('date')

        if date:
            self.validator.validate({'date': date}, {'date': 'date|date_format:%Y-%m-%d'})

            if len(self.validator.errors):
                return jsonify({
                    'error': 'Validation Error',
                    'code': 422,
                    'description': self.validator.errors
                }), 422

        uf_scraper = UfScraper(date=date)

        response = uf_scraper.make()

        if len(uf_scraper.errors):
            return jsonify({
                'error': 'Scraper Error',
                'code': 400,
                'description': uf_scraper.errors
            }), 400

        return jsonify({
            'data': {
                'uf': response
            },
            'code': 200
        }), 200

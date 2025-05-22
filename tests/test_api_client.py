import unittest, requests
import unittest.mock

from src.api_client import get_location, get_country_code, get_geo_localitation
from unittest.mock  import patch #Sirve para cambiar la funcionalidad de algo


#Los mocks se usan para simular el manejo de dependencias externas

class ApiClient(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'ipVersion': 4, 'ipAddress': '8.8.8.8', 'latitude': 37.386051, 'longitude': -122.083847, 'countryName': 'United States of America', 'countryCode': 'US', 'timeZone': '-08:00', 'zipCode': '94035', 'cityName': 'Mountain View', 'regionName': 'California', 'isProxy': False, 'continent': 'Americas', 'continentCode': 'AM', 'currency': {'code': 'USD', 'name': 'US Dollar'}, 'language': 'English', 'timeZones': ['America/Adak', 'America/Anchorage', 'America/Boise', 'America/Chicago', 'America/Denver', 'America/Detroit', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Los_Angeles', 'America/Menominee', 'America/Metlakatla', 'America/New_York', 'America/Nome', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Phoenix', 'America/Sitka', 'America/Yakutat', 'Pacific/Honolulu'], 'tlds': ['.us']}

        result = get_location("8.8.8.8")
        self.assertEqual(
            result.get("country"),
            "United States of America"
        )

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")#Con esto validamos que nuestro código esta llamando la url correcta

    @patch('src.api_client.requests.get')
    def test_get_country_code_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'ipVersion': 4, 'ipAddress': '8.8.8.8', 'latitude': 37.386051, 'longitude': -122.083847, 'countryName': 'United States of America', 'countryCode': 'US', 'timeZone': '-08:00', 'zipCode': '94035', 'cityName': 'Mountain View', 'regionName': 'California', 'isProxy': False, 'continent': 'Americas', 'continentCode': 'AM', 'currency': {'code': 'USD', 'name': 'US Dollar'}, 'language': 'English', 'timeZones': ['America/Adak', 'America/Anchorage', 'America/Boise', 'America/Chicago', 'America/Denver', 'America/Detroit', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Los_Angeles', 'America/Menominee', 'America/Metlakatla', 'America/New_York', 'America/Nome', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Phoenix', 'America/Sitka', 'America/Yakutat', 'Pacific/Honolulu'], 'tlds': ['.us']}

        result = get_country_code("8.8.8.8")
        self.assertEqual(
            result.get("countryCode"),
            "US"
        )

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service unavaible"),
            unittest.mock.Mock(
                status_code = 200,
                json = lambda: {
                    'ipVersion': 4, 'ipAddress': '8.8.8.8', 'latitude': 37.386051, 'longitude': -122.083847, 'countryName': 'United States of America', 'countryCode': 'US', 'timeZone': '-08:00', 'zipCode': '94035', 'cityName': 'Mountain View', 'regionName': 'California', 'isProxy': False, 'continent': 'Americas', 'continentCode': 'AM', 'currency': {'code': 'USD', 'name': 'US Dollar'}, 'language': 'English', 'timeZones': ['America/Adak', 'America/Anchorage', 'America/Boise', 'America/Chicago', 'America/Denver', 'America/Detroit', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Los_Angeles', 'America/Menominee', 'America/Metlakatla', 'America/New_York', 'America/Nome', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Phoenix', 'America/Sitka', 'America/Yakutat', 'Pacific/Honolulu'], 'tlds': ['.us']
                }
            )
        ]
        #mock_get.return_value.status_code = 200
        #mock_get.return_value.json.return_value = {'ipVersion': 4, 'ipAddress': '8.8.8.8', 'latitude': 37.386051, 'longitude': -122.083847, 'countryName': 'United States of America', 'countryCode': 'US', 'timeZone': '-08:00', 'zipCode': '94035', 'cityName': 'Mountain View', 'regionName': 'California', 'isProxy': False, 'continent': 'Americas', 'continentCode': 'AM', 'currency': {'code': 'USD', 'name': 'US Dollar'}, 'language': 'English', 'timeZones': ['America/Adak', 'America/Anchorage', 'America/Boise', 'America/Chicago', 'America/Denver', 'America/Detroit', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Los_Angeles', 'America/Menominee', 'America/Metlakatla', 'America/New_York', 'America/Nome', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Phoenix', 'America/Sitka', 'America/Yakutat', 'Pacific/Honolulu'], 'tlds': ['.us']}

        #método que falle cuando se llame este método
        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "United States of America")

        #mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")#Con esto validamos que nuestro código esta llamando la url correcta

    @patch('src.api_client.requests.get')
    def test_get_country_code_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'ipVersion': 4, 'ipAddress': '8.8.8.8', 'latitude': 37.386051, 'longitude': -122.083847, 'countryName': 'United States of America', 'countryCode': 'US', 'timeZone': '-08:00', 'zipCode': '94035', 'cityName': 'Mountain View', 'regionName': 'California', 'isProxy': False, 'continent': 'Americas', 'continentCode': 'AM', 'currency': {'code': 'USD', 'name': 'US Dollar'}, 'language': 'English', 'timeZones': ['America/Adak', 'America/Anchorage', 'America/Boise', 'America/Chicago', 'America/Denver', 'America/Detroit', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Los_Angeles', 'America/Menominee', 'America/Metlakatla', 'America/New_York', 'America/Nome', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Phoenix', 'America/Sitka', 'America/Yakutat', 'Pacific/Honolulu'], 'tlds': ['.us']}

        result = get_country_code("8.8.8.8")
        self.assertEqual(
            result.get("countryCode"),
            "US"
        )

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Ip not Found"),
            unittest.mock.Mock(
                status_code = 200,
                json = lambda: {
                    'ipVersion': 4, 'ipAddress': '8.8.8.8', 'latitude': 37.386051, 'longitude': -122.083847, 'countryName': 'United States of America', 'countryCode': 'US', 'timeZone': '-08:00', 'zipCode': '94035', 'cityName': 'Mountain View', 'regionName': 'California', 'isProxy': False, 'continent': 'Americas', 'continentCode': 'AM', 'currency': {'code': 'USD', 'name': 'US Dollar'}, 'language': 'English', 'timeZones': ['America/Adak', 'America/Anchorage', 'America/Boise', 'America/Chicago', 'America/Denver', 'America/Detroit', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Los_Angeles', 'America/Menominee', 'America/Metlakatla', 'America/New_York', 'America/Nome', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Phoenix', 'America/Sitka', 'America/Yakutat', 'Pacific/Honolulu'], 'tlds': ['.us']
                }
            )
        ]

        #método que falle cuando se llame este método
        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "United States of America")

    @patch('src.api_client.requests.get')
    def test_get_geolocalitation_data_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Ip not Found"),
            unittest.mock.Mock(
                status_code = 200,
                json = lambda: {
                    'ipVersion': 4, 'ipAddress': '8.8.8.8', 'latitude': 37.386051, 'longitude': -122.083847, 'countryName': 'United States of America', 'countryCode': 'US', 'timeZone': '-08:00', 'zipCode': '94035', 'cityName': 'Mountain View', 'regionName': 'California', 'isProxy': False, 'continent': 'Americas', 'continentCode': 'AM', 'currency': {'code': 'USD', 'name': 'US Dollar'}, 'language': 'English', 'timeZones': ['America/Adak', 'America/Anchorage', 'America/Boise', 'America/Chicago', 'America/Denver', 'America/Detroit', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Los_Angeles', 'America/Menominee', 'America/Metlakatla', 'America/New_York', 'America/Nome', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Phoenix', 'America/Sitka', 'America/Yakutat', 'Pacific/Honolulu'], 'tlds': ['.us']
                }
            )
        ]

        # Método para representar el fallo cuando se llame a ese método
        with self.assertRaises(requests.exceptions.RequestException):
            get_geo_localitation("8.8.8.8")

        result = get_geo_localitation("8.8.8.8")
        self.assertEqual(result.get('latitude'), 37.386051)
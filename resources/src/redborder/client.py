# Copyright (C) 2023 Eneo Tecnologia S.L.
#
# Authors :
# Miguel Álvarez Adsuara <malvarez@redborder.com>
# Pablo Rodriguez Flores <prodriguez@redborder.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests

class RedBorderAPI:
    def __init__(self, endpoint, oauth_token) -> None:
        self.api_endpoint = endpoint
        self.oauth_token = oauth_token

    def request_flow_sensors(self):
        response = requests.get(f'{self.api_endpoint}/sensors/flow/?auth_token={self.oauth_token}')

        if response.status_code == 200:
            response_json = response.json()
            return response_json['flow']

        raise Exception(f"redBorder api request failed with status code {response.status_code}.")

# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for SignJwt
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-iam-credentials


# [START iamcredentials_generated_credentials_v1_IAMCredentials_SignJwt_async]
from google.iam import credentials_v1


async def sample_sign_jwt():
    """Snippet for sign_jwt"""

    # Create a client
    client = credentials_v1.IAMCredentialsAsyncClient()

    # Initialize request argument(s)
    request = credentials_v1.SignJwtRequest(
        name="projects/{project}/serviceAccounts/{service_account}",
        payload="payload_value",
    )

    # Make the request
    response = await client.sign_jwt(request=request)

    # Handle response
    print(response)

# [END iamcredentials_generated_credentials_v1_IAMCredentials_SignJwt_async]

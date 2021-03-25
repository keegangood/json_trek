# JSON Trek
## Star-Trek-flavored JSON data

Generate fake JSON user data and lorem ipsum with a Star Trek theme.

## Fake User Data

JSON Trek can generate user information for the following categories:

- Username
- Email address
- First name
- Last name
- Address
  - Street
  - City
  - State
  - Country
  - Zip code
- Occupation

```python
from json_trek import JSONTrek

trek = JSONTrek()

# receive a user profile with all fields
profile = trek.user_profile()


# or, pass a list of the desired user profile fields
trek.user_profile([
    'username',
    'email',
])
```

## Human / Klingon Ipsum

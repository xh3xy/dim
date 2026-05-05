from django.http import JsonResponse
from django.views import View
from pathlib import Path
import semver
import tomllib


class ServerVersion(View):
    def get(self, request):
        current = Path(__file__).resolve().parent
        while current != current.parent:
            candidate = current / 'pyproject.toml'
            if candidate.exists():
                break
            current = current.parent
        else:
            raise FileNotFoundError('pyproject.toml missing')

        with open(candidate, 'rb') as f:
            data = tomllib.load(f)

        ver = semver.Version.parse(data['project']['version'])

        return JsonResponse({
            'major': ver.major,
            'minor': ver.minor,
            'patch': ver.patch,
        })
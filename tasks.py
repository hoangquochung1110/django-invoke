from invoke.collection import Collection

import django_invoke


ns = Collection(
    django_invoke.docker,
    django_invoke.django,
)


# Configurations for run command
ns.configure(
    {
        "run": {
            "pty": True,
            "echo": True,
        },
        "django_invoke": django_invoke._config.Config(
            project_name="django_invoke",
            django=django_invoke.DjangoSettings(
                manage_file_path="/Users/hunghoang/Development/cs50w-network/manage.py",
                settings_path="project4.local",
            ),
        )
    },
)

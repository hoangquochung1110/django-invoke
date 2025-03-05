import dataclasses
import collections

import invoke


@dataclasses.dataclass
class DockerSettings:
    main_containers: collections.abc.Sequence[str] = (
        "postgres",
        "redis",
    )
    compose_cmd = "docker-compose"


@dataclasses.dataclass(frozen=True)
class Config:
    project_name: str = ""

    docker: DockerSettings = dataclasses.field(
        default_factory=DockerSettings,
    )

    @classmethod
    def from_context(cls, context: invoke.Context) -> "Config":
        """Get config from invoke context."""
        return context.config.get(
            "django_invoke",
            cls(),
        )

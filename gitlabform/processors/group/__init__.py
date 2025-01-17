from typing import List

from gitlabform.configuration import Configuration
from gitlabform.gitlab import GitLab
from gitlabform.processors import AbstractProcessors
from gitlabform.processors.abstract_processor import AbstractProcessor
from gitlabform.processors.group.group_badges_processor import GroupBadgesProcessor
from gitlabform.processors.group.group_ldap_links_processor import (
    GroupLDAPLinksProcessor,
)
from gitlabform.processors.group.group_members_processor import (
    GroupMembersProcessor,
)
from gitlabform.processors.group.group_shared_with_processor import (
    GroupSharedWithProcessor,
)
from gitlabform.processors.group.group_secret_variables_processor import (
    GroupSecretVariablesProcessor,
)
from gitlabform.processors.group.group_settings_processor import (
    GroupSettingsProcessor,
)


class GroupProcessors(AbstractProcessors):
    def __init__(self, gitlab: GitLab, config: Configuration, strict: bool):
        super().__init__(gitlab, config, strict)
        self.processors: List[AbstractProcessor] = [
            GroupSecretVariablesProcessor(gitlab),
            GroupSettingsProcessor(gitlab),
            GroupMembersProcessor(gitlab),
            GroupSharedWithProcessor(gitlab),
            GroupLDAPLinksProcessor(gitlab),
            GroupBadgesProcessor(gitlab),
        ]

class AIPlaybookError(Exception):
    """Base error for playbook operations."""


class AuthenticationError(AIPlaybookError):
    pass


class RateLimitError(AIPlaybookError):
    pass


class ProviderUnavailableError(AIPlaybookError):
    pass


class BudgetExceededError(AIPlaybookError):
    pass


class OutputValidationError(AIPlaybookError):
    pass

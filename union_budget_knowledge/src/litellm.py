# Minimal stub for litellm to allow project to run without full package install
# (disk space constraints)

def completion(model=None, messages=None, **kwargs):
    """Stub completion function that returns a mock response."""
    return {
        "choices": [
            {
                "message": {
                    "content": "Mock response from litellm stub. Install the full litellm package for real LLM calls."
                }
            }
        ]
    }

__all__ = ["completion"]

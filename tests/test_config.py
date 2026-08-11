from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from ai_leetcode.config import load_identity, load_profiles


class ProfileConfigTests(unittest.TestCase):
    def test_explicit_profile_controls_model_and_reasoning_effort(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "config").mkdir()
            (root / "config" / "profiles.json").write_text(
                json.dumps(
                    {
                        "defaultProfile": "sol-medium",
                        "profiles": [
                            {
                                "id": "sol-medium",
                                "model": "gpt-5.6-sol",
                                "reasoningEffort": "medium",
                                "cohort": "sol-escalation",
                                "stage": 1,
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (root / ".ai").mkdir()
            (root / ".ai" / "identity.env").write_text(
                "AI_CLIENT_NAME=test-client\nAI_MODEL_NAME=wrong-model\n",
                encoding="utf-8",
            )
            clean_environment = {
                key: value
                for key, value in os.environ.items()
                if key not in {"AI_CLIENT_NAME", "AI_MODEL_NAME", "AI_PROFILE_ID", "AI_REASONING_EFFORT"}
            }
            with patch.dict(os.environ, clean_environment, clear=True):
                identity = load_identity(root, profile_id="sol-medium")

            assert identity is not None
            self.assertEqual(identity.client, "test-client")
            self.assertEqual(identity.model, "gpt-5.6-sol")
            self.assertEqual(identity.reasoning_effort, "medium")
            self.assertEqual(identity.profile_id, "sol-medium")
            self.assertEqual(load_profiles(root).default_profile, "sol-medium")


if __name__ == "__main__":
    unittest.main()

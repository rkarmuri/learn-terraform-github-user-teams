# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

provider "github" {
token = "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"
organization = "test-oss-terraform"
}

# Retrieve information about the currently (PAT) authenticated user
data "github_user" "self" {
  username = ""
}

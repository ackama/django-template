---
tags:
    - tasks
---
# Test CI Workflows Locally

For developers familiar with GitHub Actions but looking to streamline their CI testing process locally, `act` offers a practical solution. Here’s how to leverage `act` for local CI workflow testing:

## Requirements
- `act` installed on your machine. For installation, see the [`act` User Guide][act-user-guide].

## Using `act` for Local Workflow Testing

1. **Ensure `act` is Installed**: Confirm `act` is set up on your system. If you’re unsure, run `act -h` in your terminal to check for its presence.

2. **Prepare Your Project**: Navigate to your project’s root directory in the terminal, ensuring you’re in the same location as your `.github` workflow directory.

3. **Execute a Workflow with `act`**:
    - To simulate a `push` event, use:

      ```shell
      act push --container-architecture linux/amd64
      ```

    - Substitute `push` with any event relevant to your workflows, such as `pull_request`, if needed.
    - Adjust `--container-architecture` as per your project's or local setup's needs (e.g., `linux/arm64` for ARM-based systems).

4. **Analyze the Execution Output**: Examine the terminal output for insights into the workflow execution, and adjust your workflow files or code based on the feedback provided.

### Tips for Efficient Use

- **Iterate Quickly**: Use `act` to rapidly test changes to your workflows without pushing to GitHub, saving time and avoiding unnecessary commits.
- **Customization**: Tailor the `act` command with additional flags as needed for your specific testing scenario, such as specifying a different GitHub event or workflow file.

By integrating `act` into your local development workflow, you gain a powerful tool for preemptively identifying and fixing issues in your CI process, enhancing overall efficiency and reliability.

[act-user-guide]: https://github.com/nektos/act#readme
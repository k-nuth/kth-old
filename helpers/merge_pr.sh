#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 branch_name"
    exit 1
fi

branch_name=$1

submodules=(
    "domain"
    # "infrastructure"
    # "database"
    # "network"
    # "consensus"
    # "blockchain"
    # "node"
    # "node-exe"
    # "c-api"
    # "secp256k1"
)

merge_pr() {
    submodule=$1
    cd $submodule || exit 1

    pr_url=$(gh pr list --base master --head "$branch_name" --json url --jq '.[0].url')

    if [ -n "$pr_url" ]; then
        echo "Merging PR in $submodule..."
        gh pr merge "$pr_url" --merge --delete-branch
        echo "PR merged in $submodule."
    else
        echo "No PR found for branch $branch_name in $submodule."
        exit 1
    fi

    git checkout master
    git pull origin master

    cd - > /dev/null
}

for submodule in "${submodules[@]}"; do
    echo "Processing $submodule..."
    merge_pr $submodule
done

echo "Proceso de merge completado para todos los submódulos."

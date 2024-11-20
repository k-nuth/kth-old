#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 branch_name commit_message"
    exit 1
fi

branch_name=$1
commit_message=$2

submodules=(
    "domain"
    "infrastructure"
    # "database"
    # "network"
    # "consensus"
    # "blockchain"
    # "node"
    # "node-exe"
    "c-api"
    # "secp256k1"
)

finalize_submodule() {
    submodule=$1
    cd $submodule || exit 1

    git add .
    git commit -m "$commit_message"
    git push -u origin $branch_name

    # gh pr create --title "$commit_message in $submodule" --body "Automated update" --base master
    gh pr create --title "$commit_message in $submodule" --body "" --base master

    cd - > /dev/null
}

for submodule in "${submodules[@]}"; do
    echo "Finalizando PR para $submodule..."
    finalize_submodule $submodule
    echo "PR creado para $submodule."
done

echo "Todos los PRs están creados. Recuerda aprobar y mergear cada PR manualmente."

#!/bin/bash
set -e

if [ -z "$1" ]; then
    echo "Usage: $0 branch_name"
    exit 1
fi

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

branch_name=$1

prepare_submodule() {
    submodule=$1
    cd $submodule || exit 1

    if [[ -n $(git status --porcelain) ]]; then
        echo "Error: There are local changes in $submodule. Commit or discard changes before continuing."
        exit 1
    fi

    git checkout master
    git pull origin master

    if git show-ref --verify --quiet refs/heads/$branch_name; then
        echo "Error: Branch $branch_name already exists in $submodule."
        exit 1
    fi

    echo "Creating branch $branch_name in $submodule."
    git checkout -b $branch_name

    cd - > /dev/null
}

# Itera sobre cada submódulo
for submodule in "${submodules[@]}"; do
    echo "Preparando $submodule..."
    prepare_submodule $submodule
    echo "$submodule preparado en el branch $branch_name."
done

echo "Todos los submódulos están listos para hacer los cambios necesarios."

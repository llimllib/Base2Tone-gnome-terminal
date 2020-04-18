#!/usr/bin/env bash
set -euxo pipefail

python map_templates.py

if ! command -v base16-builder >/dev/null 2>&1; then
    echo "base16-builder is not installed; install nodejs then:"
    echo "  npm install -g base16-builder"
    exit 1
fi

rm -rf gnome-theme-scripts/*
for scheme in schemes/*.yml ; do
    base=$(basename "$scheme")
    for template in templates/*_2tone.ejs ; do
        type=$(basename "$template")
        base16-builder -t "$template" -s "$scheme" > gnome-theme-scripts/"${base%%.*}"-"${type%%_*}".sh
    done
done
chmod a+x gnome-theme-scripts/*.sh

#!/bin/bash

json_name=$1

set -x
filename=$(echo "$json_name" | cut -d\. -f1)
sets_name=($(jq 'keys[]' ${json_name} | sed "s/\"//g"))
echo $sets_name
for set_name in "${sets_name[@]}"; do
set +x
    txts=($(jq --arg set_name $set_name ".$set_name[][1]" $json_name | sed "s/\"//g"))

    mkdir -p $filename/$set_name/txt 
    mkdir -p $filename/$set_name/png 
    echo $txts
    for txt in "${txts[@]}"; do
        cp "$txt" "${filename}/${set_name}/txt"
    done
    echo "Done copying txts in ${set_name}"

    unset txts
    pngs=($(jq --arg set_name $set_name ".$set_name[][0]" frame_txt_sec1.json | sed "s/\"//g"))
    for png in "${pngs[@]}"; do
        cp "$png" "${filename}/${set_name}/png"
    done
    echo "Done copying pngs in ${set_name}"
done

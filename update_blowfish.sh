version="2.98.0"
proxy="http://127.0.0.1:7897"

source_url="https://github.com/nunocoracao/blowfish/archive/refs/tags/v$version.zip"
output_dir="$(dirname "$(realpath "$0")")/themes"

curl "$source_url" \
    -L \
    -o "$output_dir/blowfish-$version.zip" \
    -x "$proxy"

unzip "$output_dir/blowfish-$version.zip" -d "$output_dir"
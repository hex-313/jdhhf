function dl-and-stream() {
  aria2c "$1" &
  file="$(ls -1t | head -n1)"
  mpv "$file"
}

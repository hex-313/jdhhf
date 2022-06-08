# Downloader Function
startDownload() {
    clear
    case $downloadType in
        "Torrent")
            aria2c --seed-time=0 --max-upload-limit=5K "$url"
        ;;
        "File")
            aria2c -o "$name" "$url"
        ;;
    esac
}

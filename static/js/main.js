function getCookie(name) {
    let cookies = document.cookie.split("; ")
    return cookies.find(c => c.startsWith(name))
        .split("=")[1]
        .replaceAll("\"","")

}


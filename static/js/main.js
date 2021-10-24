function getCookie(name) {
    let cookies = document.cookie.split("; ")
    return cookies.find(c => c.startsWith(name))
        .split("=")[1]
        .replaceAll("\"","")
}

function fixedTime(sec) {
    let clock = new Date(sec * 1000)
    return [clock.getUTCHours(), clock.getMinutes(), clock.getSeconds()].map(v => v.toString().padStart(2, '0'))
}

const check = done => done
    ? '<i class="fas fa-check-circle"></i>'
    : '<i class="far fa-check-circle"></i>'

function toggleList() {
    let toggleBtn = document.querySelector(".detail-toggle")
    let targetList = document.querySelector(".round-week-detail-body")
    if (toggleBtn.textContent === "목록 닫기") {
        toggleBtn.textContent = "목록 열기"
    } else {
        toggleBtn.textContent = "목록 닫기"
    }
    document.querySelector("i.fas.fa-chevron-up").classList.toggle("is-hidden")
    document.querySelector("i.fas.fa-chevron-down").classList.toggle("is-hidden")
    targetList.classList.toggle("is-hidden")
}

function getCourseListForRoadmap() {
    fetch("/api/courses")
        .then((resp) => resp.json())
        .then((response) => {
            document.querySelector(".summary-title").textContent = response["course_title"]
            let div = document.querySelector(".round-week-detail-body")
            let totalPlaytime = 0
            let seenIndex = 0
            response["courses"].forEach((klass) => {
                let {title, done, order, week, week_order, playtime} = klass
                if (done) seenIndex = order;
                let playtimeFixed = fixedTime(playtime)[1] + ":" + fixedTime(playtime)[2]
                div.innerHTML += `
                    <div class="week-body" onclick="openCourse(${order})">
                        <div class="week-detail-num">${week}-${week_order}</div>
                        <div class="week-detail-title">[${week} 주차] ${title}</div>
                        <div class="week-detail-playtime">${playtimeFixed}</div>
                        <div class="week-detail-seen">${check(done)}</div>
                    </div>`
                totalPlaytime += playtime
            })
            document.querySelectorAll(".week-body")[seenIndex - 1].classList.add('highlighted')
            document.querySelector(".detail-obj").innerHTML = '<i class="fas fa-clock"></i>' +
                fixedTime(totalPlaytime)[0] + "시간 " + fixedTime(totalPlaytime)[1] + "분"
        })
        .catch((err) => console.warn(err))
}

function getDataForEnrollment(courseName) {
    fetch(`/api/enrollment?title=${courseName}`)
        .then((resp) => resp.json())
        .then((response) => {
            let {price, discount_ratio} = response
            let originPrice = price
            let discounting = price * discount_ratio
            let discounted = price - discounting
            let installment = discounted / 6
            let [first, second, third] = document.querySelectorAll("div.payment-info-right")
            first.textContent = originPrice.toLocaleString() + " 원"
            second.textContent = "- " + discounting.toLocaleString() + " 원"
            third.textContent = discounted.toLocaleString() + " 원"
            document.querySelector(".installment-discount").textContent = (discount_ratio * 100).toFixed() + "% "
            document.querySelector(".installment-price span").textContent = installment.toLocaleString("ko", {maximumFractionDigits: 0})
        }).catch((error)=>console.warn(error))
}

function enrollment() {
    const body = JSON.stringify({courseName, mode: "cors"})
    const init = {method: "POST", body}
    fetch("/api/enrollment", init)
        .then((resp) => resp.json())
        .then((response) => {
            if (response.message) {
                window.location.href = "/roadmap"
            }
        })
        .catch((err) => console.error(err))
}

function openCourse(order) {
    const body = JSON.stringify({order, mode: "cors"})
    const init = {method: "POST", body}
    fetch("/api/courses", init)
        .then((resp) => resp.json())
        .then((response) => {
            if (response["message"] !== "success") {
                alert(response.message)
                window.location.reload()
            } else {
                let {lecture_id} = response
                window.location.href = `/lecture/${lecture_id}`
            }
        })
        .catch((err) => console.error(err))
}

function lectureNav() {
    fetch("/api/courses")
        .then((resp) => resp.json())
        .then((response) => {
            let div = document.querySelector(".week-detail-list")
            let seenIndex = 0
            response["courses"].forEach((klass) => {
                let {title, done, order, week, week_order} = klass
                if (done) seenIndex = order;
                div.innerHTML += `
                    <div class="week-detail">
                        <div class="">${week}-${week_order}</div>
                        <div class="text">${title}</div>
                        <i class="${done ? "fas" : "far"} fa-check-circle"></i>
                    </div>`
            })
        })
        .catch((err) => console.warn(err))
}
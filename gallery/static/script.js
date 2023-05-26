// global properties to use in our script
generateCards()
let startButton = document.getElementById("start-clear-button")
let timerValue = document.getElementById("timer")
let resultLine = document.getElementById("result-count")
let backSides = document.querySelectorAll(".flip-box-back")
let oneMin = 200
let num = !NaN
let numArr = []
let clickCounter = 0
let progressCount = 0
let firstCardValue
let secondCardValue
let firstCard
let secondCard

// array numbers random filling
for (let i = 1; i <= 14; i++) {
    numArr.push(i, i)
}
numArr.sort(() => 0.5 - Math.random());
let imagePath = "./static/artists_img/";
addBackNum(imagePath)

//numbers adding func
function addBackNum(imagePath) {
    let a = 0
    for (let blackSide of backSides) {
        blackSide.textContent = numArr[a]
        console.log(numArr[a])
        let imageName = numArr[a].toString() + ".jpg";
        let fullPath = `${imagePath}${imageName}`;
        blackSide.style.backgroundImage = `url('${fullPath}')`;
        blackSide.style.backgroundSize = "95% 95%"
        blackSide.style.backgroundRepeat = "no-repeat"
        blackSide.style.color = "transparent";
        a++
    }
}

// adding background image for all card ellements here, istead of .css file
function generateCards() {
    let cards = document.querySelectorAll(".card")
    for (let card of cards) {
        card.style.backgroundImage = "url('./static/backCardImg.png')"
        card.style.backgroundSize = "95% 95%"
        card.style.backgroundRepeat = "no-repeat"
    }
}


// time counting function with start button and calling for main function
startButton.addEventListener('click', function () {
    interval = setInterval(myTimer, 1000);
});

function myTimer() {
    cardsMatchingFunc()
    oneMin = oneMin - 1;
    timerValue.innerHTML = oneMin + " sec"
    if (oneMin == 0) {
        oneMin = 10
        timerValue.innerHTML = "Try more"
        clearInterval(interval)
        resetMatching()
    }
}

//adding numbers for fliping cards
function cardsMatchingFunc() {
    let flBxs = document.querySelectorAll(".flip-box")
    for (let flBx of flBxs){
        flBx.addEventListener('click', flipCards)
    }
}

//fliping cards
function flipCards(e) {
    e.target.parentNode.parentNode.classList.add("active")
    clickCounter++
    if (clickCounter == 1) {
        firstCardValue = e.target.nextElementSibling.innerHTML
        firstCard = e.target
        console.log("firstCard  ",firstCardValue);
    } else {
        secondCardValue = e.target.nextElementSibling.innerHTML
        console.log("secondCard  ",secondCardValue);
        if(firstCardValue == secondCardValue){
        e.target.parentNode.parentNode.classList.add("match")
        firstCard.parentNode.parentNode.classList.add("match")
        progressCount++
        //matching cards
        progResFunc()
    }else{
        let flBxs = document.querySelectorAll(".flip-box")
        flBxs.forEach((item) => {
        setTimeout(function () {
            item.classList.remove("active")
        }, 500)
    })
    clickCounter = 0
  }
 }
}

// Cpunting and result pushing
function progResFunc(){
    let res = progressCount*100/14
    resultLine.innerHTML = Math.round(res) + " %"
    if(Math.round(res) == 100){
        alert("You simply the best")
        resetMatching()
    }
}

//reset function (end game)
function resetMatching(){
    let flBxs = document.querySelectorAll(".flip-box")
        flBxs.forEach((item) => {item.classList.remove("active")})
        flBxs.forEach((item) => {item.classList.remove("match")})
        for (let flBx of flBxs) {
            flBx.removeEventListener('click', flipCards)
        }
        resultLine.innerHTML = "one more try ?"
        clearInterval(interval)
        oneMin = 200
}
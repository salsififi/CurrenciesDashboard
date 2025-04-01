/**
 * Make currency/templates/currency/index.html dynamic
 */

const data = JSON.parse(document.getElementById("data").textContent)
const daysLabels = JSON.parse(document.getElementById("days_labels").textContent)

/**
 * Display charts for all selected currencies
 */
function displayCharts() {
    for (const [currency, rates] of Object.entries(data)) {
        const canvasChart = document.getElementById(`chart-${currency}`)
        new Chart(canvasChart, {
            type: "line",
            data: {
                labels: daysLabels,
                datasets: [{
                    label: currency,
                    data: rates,
                    fill: false,
                    borderColor: "rgb(255, 128, 128)",
                    trendlineLinear: {
                        colorMin: "#00ff00",
                        colorMax: "#ff00ff",
                        width: 1,
                        lineStyle: "dotted",
                    }
                }]
            }
        })
    }
}

/**
 * Split an url
 * @param {string} url - url to split
 * @returns {(*|string)[]|string[]} - array containing both segments
 */
function splitUrl(url) {
    const separator = "currencies="
    const separatorIndex = url.indexOf(separator)
    if (separatorIndex !== -1) {
        const beforLastSegment = url.substring(0, separatorIndex + separator.length)
        const lastSegment = url.substring(separatorIndex + separator.length)
        return [beforLastSegment, lastSegment]
    }
    return [url, ""]
}

/**
 * Manage currencies toggle buttons to modify url when clicked
 */
function manageCurrenciesButtons() {
    const aCurrenciesList = document
        .getElementById("currencies-buttons")
        .querySelectorAll("a")
    aCurrenciesList.forEach((elem) => {
        elem.addEventListener("click", () => {
            const currentUrl = window.location.href
            let [beforLastSegment, lastSegment] = splitUrl(currentUrl)
            let currenciesArray = lastSegment.split(",")
            let currencyIndex = currenciesArray.indexOf(elem.innerText)
            let hasChanged = false
            if (currencyIndex === -1) {
                currenciesArray.push(elem.innerText)
                hasChanged = true
            } else {
                if (currenciesArray.length > 1) {
                    currenciesArray.splice(currencyIndex, 1)
                    hasChanged = true
                }
            }
            lastSegment = currenciesArray.join(",")
            elem.href = beforLastSegment + lastSegment
            if (hasChanged) {
                elem.classList.toggle("btn-info")
                elem.classList.toggle("btn-secondary")
            }
        })
    })
}

manageCurrenciesButtons()
displayCharts(window.location.href)

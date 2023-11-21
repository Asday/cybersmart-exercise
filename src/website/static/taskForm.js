const weatherReports = JSON.parse(
  document.querySelector("#weatherReports").textContent,
)

const colorsToClasses = {
  "red": "bg-danger",
  "yellow": "bg-primary",
  "blue": "bg-info",
}

const updateTemperatureAndBG = (select, temperature, container) => {
  container.classList.remove("text-white")
  container.classList.remove("bg-danger")
  container.classList.remove("bg-primary")
  container.classList.remove("bg-info")

  const report = weatherReports[select.value]
  if (report === undefined) {
    temperature.textContent = "--"

    return
  }

  temperature.textContent = report.celcius
  container.classList.add("text-white")
  container.classList.add(colorsToClasses[report.color])
}

window.ready(() => {
  document.querySelectorAll(".js-location-select").forEach((el) => {
    const sel = el.querySelector("select")
    const temp = el.querySelector(".js-temperature")
    sel.addEventListener("change", () => updateTemperatureAndBG(sel, temp, el))

    updateTemperatureAndBG(sel, temp, el)
  })
})

document.getElementById("grade").addEventListener("click", function () {
  var q1 = document.querySelector("input[name=q1]:checked");
  var q2 = document.querySelector("input[name=q2]:checked");
  var result = document.getElementById("result");
  if (!q1 || !q2) {
    result.textContent = "Choose an answer for both questions.";
    return;
  }
  var score = (q1.value === "b" ? 1 : 0) + (q2.value === "app" ? 1 : 0);
  result.textContent = score + "/2. Urgency plus a lookalike link is the pattern. Open the app you already trust.";
});

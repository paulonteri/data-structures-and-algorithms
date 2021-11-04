// https://leetcode.com/discuss/general-discussion/1541618/remove-all-easymedium-questions-from-leetcode-company-problems-page-after-sorting-by-frequency

function removeAll(label) {
    var cont = true;
    while (cont) {
        const success_span = document.querySelector(label);
        if (success_span) {
            success_span.closest("tr").remove();
        } else {
            cont = false;
        }
    }
}
// hard -> .label-danger
// medium -> .label_warning
// easy -> .label-success
removeAll(".label-success");

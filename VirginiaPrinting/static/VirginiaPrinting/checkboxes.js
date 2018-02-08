var checkboxes_bios = document.querySelectorAll('input.suboption_bios'),
    checkall_bios = document.getElementById('biographies'),
    checkboxes_imprints = document.querySelectorAll('input.suboption_imprints'),
    checkall_imprints = document.getElementById('imprints'),
    checkboxes_news_cites = document.querySelectorAll('input.suboption_news_cites'),
    checkall_news_cites = document.getElementById('news_cites'),
    checkboxes_news_hists = document.querySelectorAll('input.suboption_news_hists'),
    checkall_news_hists = document.getElementById('news_hists');

for(var i=0; i<checkboxes_bios.length; i++) {
  checkboxes_bios[i].onclick = function() {
    var checkedCount = document.querySelectorAll('input.suboption_bios:checked').length;

    checkall_bios.checked = checkedCount > 0;
    checkall_bios.indeterminate = checkedCount > 0 && checkedCount < checkboxes_bios.length;
  }
}

for(var i=0; i<checkboxes_imprints.length; i++) {
  checkboxes_imprints[i].onclick = function() {
    var checkedCount = document.querySelectorAll('input.suboption_imprints:checked').length;

    checkall_imprints.checked = checkedCount > 0;
    checkall_imprints.indeterminate = checkedCount > 0 && checkedCount < checkboxes_imprints.length;
  }
}

for(var i=0; i<checkboxes_news_cites.length; i++) {
  checkboxes_news_cites[i].onclick = function() {
    var checkedCount = document.querySelectorAll('input.suboption_news_cites:checked').length;

    checkall_news_cites.checked = checkedCount > 0;
    checkall_news_cites.indeterminate = checkedCount > 0 && checkedCount < checkboxes_news_cites.length;
  }
}

for(var i=0; i<checkboxes_news_hists.length; i++) {
  checkboxes_news_hists[i].onclick = function() {
    var checkedCount = document.querySelectorAll('input.suboption_news_hists:checked').length;

    checkall_news_hists.checked = checkedCount > 0;
    checkall_news_hists.indeterminate = checkedCount > 0 && checkedCount < checkboxes_news_hists.length;
  }
}

checkall_bios.onclick = function() {
    for (var i = 0; i < checkboxes_bios.length; i++) {
        checkboxes_bios[i].checked = this.checked;
    }
}

checkall_imprints.onclick = function() {
    for (var i = 0; i < checkboxes_imprints.length; i++) {
        checkboxes_imprints[i].checked = this.checked;
    }
}

checkall_news_cites.onclick = function() {
    for (var i = 0; i < checkboxes_news_cites.length; i++) {
        checkboxes_news_cites[i].checked = this.checked;
    }
}

checkall_news_hists.onclick = function() {
    for (var i = 0; i < checkboxes_news_hists.length; i++) {
        checkboxes_news_hists[i].checked = this.checked;
    }
}
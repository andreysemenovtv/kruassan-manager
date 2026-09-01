(function(){
  var ua=navigator.userAgent||'';
  var isIOS=/iPad|iPhone|iPod/i.test(ua)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
  if(isIOS){
    window.__TRAINING_LITE__=true;
    document.write('<script src="training-data-lite.js?v=3"><\/script>');
  }
})();

(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2caa3c59"],{2957:function(t,e,n){"use strict";var r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("md-card",{attrs:{"md-with-hover":""}},[n("md-ripple",[n("md-card-header",[n("md-card-media",[n("img",{attrs:{src:t.account.avatar,alt:"People"}})]),n("md-card-header-text",[n("div",{staticClass:"md-title"},[t._v(t._s(t.account.first_name)+" "+t._s(t.account.last_name))])])],1)],1)],1)},a=[],c={name:"UserCard",props:{account:Object}},i=c,s=(n("809f"),n("2877")),o=Object(s["a"])(i,r,a,!1,null,"58212640",null);e["a"]=o.exports},"386b":function(t,e,n){var r=n("5ca1"),a=n("79e5"),c=n("be13"),i=/"/g,s=function(t,e,n,r){var a=String(c(t)),s="<"+e;return""!==n&&(s+=" "+n+'="'+String(r).replace(i,"&quot;")+'"'),s+">"+a+"</"+e+">"};t.exports=function(t,e){var n={};n[t]=e(s),r(r.P+r.F*a(function(){var e=""[t]('"');return e!==e.toLowerCase()||e.split('"').length>3}),"String",n)}},"595a":function(t,e,n){},"809f":function(t,e,n){"use strict";var r=n("595a"),a=n.n(r);a.a},b54a:function(t,e,n){"use strict";n("386b")("link",function(t){return function(e){return t(this,"a","href",e)}})},ed36:function(t,e,n){"use strict";n.r(e);var r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticStyle:{width:"100%"}},t._l(t.deletedFriends,function(e){return n("user-card",{key:e.id,attrs:{account:e},nativeOn:{click:function(e){return t.clickOnUser(t.index)}}})}),1)},a=[],c=(n("b54a"),n("2957")),i={name:"Deleted",components:{UserCard:c["a"]},computed:{deletedFriends:function(){return this.$store.state.deletedFriends}},methods:{clickOnUser:function(t){this.openInNewTab(this.$store.state.abandonedFriends[t].link)},openInNewTab:function(t){var e=window.open(t,"_blank");e.focus()}}},s=i,o=n("2877"),u=Object(o["a"])(s,r,a,!1,null,"518cffb9",null);e["default"]=u.exports}}]);
//# sourceMappingURL=chunk-2caa3c59.23bdd55e.js.map
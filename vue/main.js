var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!'
    }
});


var app2 = new Vue({
    el: '#app2',
    data: {
        message: new Date().toLocaleString()
    }
})


var app6 = new Vue({
    el: '#app3',
    data: {
        message: 'Hello Vue!'
    },
    methods: {
        reverseMessage: function () {
            this.message = this.message.split('').reverse().join('')
        }
    }
})
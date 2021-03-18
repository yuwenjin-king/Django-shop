let vm = new Vue({
    el:'#app',
    data:{
        //v-model
        username : '',
        password: '',
        password2: '',
        mobile: '',
        allow: '',
        //v-show
        error_name:false,
        error_password:false,
        sms_code_tip:false,
        error_sms_code_message:false,

        //error_message
        // error_name_message
        // error_phone_message
        // sms_code_tip
        // error_sms_code_message
    },
    method:{
        check_username(){
        let re = '/^[a-zA-z0-9]'
        if (re.test(this.username)) {
            this.error_name = false;
        }else {
            this.error_name_message = '请输入5-20个字符'
            this.error_name = true;
        }
}
    }
})
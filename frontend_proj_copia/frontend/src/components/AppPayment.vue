<template>
  <div v-if="show" id="size_adjust" class="popup_minuta">
    <div class="popup_content">
      <span class="main_title">Coloque dados do seu cartão</span>
      <div class="security_subtitle">
        <div class="card_available_img"></div>
        <div class="security_img"></div>
        <div class="sub_title">Seus dados estão seguros</div>
      </div>
      <div class="input_group" v-for="(campo, index) in campos" :key="index">
        <input
          type="text"
          class="input_payment_popup"
          v-model="cartao[campo.model]"
          :id="'input_' + campo.model"
          @focus="campo.focused = true"
          @blur="onBlur(campo)"
        />
        <label
          :for="'input_' + campo.model"
          :class="{ float: campo.focused || cartao[campo.model] }"
        >
          {{ campo.label }}
        </label>
      </div>

      <div class="input_group">
        <div style="display: flex; gap: 1rem;">
          <div class="input_group" style="flex: 1;">
            <input
              type="text"
              class="input_payment_popup"
              v-model="cartao.MM"
              id="input_MM"
              @focus="valFocus.MM = true"
              @blur="onBlurVal('MM')"
    
            />
            <label
              for="input_MM"
              :class="{ float: valFocus.MM || cartao.MM }"
            >
              MM
            </label>
          </div>
          <div class="input_group" style="flex: 1;">
            <input
              type="text"
              class="input_payment_popup"
              v-model="cartao.YY"
              id="input_YY"
              @focus="valFocus.YY = true"
              @blur="onBlurVal('YY')"
          
            />
            <label
              for="input_YY"
              :class="{ float: valFocus.YY || cartao.YY }"
            >
              YY
            </label>
          </div>
        </div>
      </div>

      <div class="input_group">
        <input
          type="text"
          class="input_payment_popup"
          v-model="cartao.CVV"
          id="input_CVV"
          @focus="cvvFocus = true"
          @blur="onBlurCVV"
        />
        <label
          for="input_CVV"
          :class="{ float: cvvFocus || cartao.CVV }"
        >
          CVV
        </label>
      </div>

      <div style="margin-top: 1rem;">
        <button class="btn_pagar" @click="confirmarPagamento">
          Confirmar Pagamento
        </button>
        <button class="btn_cancel" @click="$emit('fechar')"></button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppPayment",
  props: {
    show: Boolean
  },
  data() {
    return {
      cartao: {
        numero: '',
        nome: '',
        MM: '',
        YY: '',
        CVV: ''
      },
      campos: [
        { label: 'Número do Cartão', model: 'numero', focused: false },
        { label: 'Nome do Titular', model: 'nome', focused: false }
      ],
      valFocus: {
        MM: false,
        YY: false
      },
      cvvFocus: false
    };
  },
  methods: {
    confirmarPagamento() {
      this.$emit('submeter', this.cartao);
    },
    onBlur(campo) {
      if (!this.cartao[campo.model]) {
        campo.focused = false;
      }
    },
    onBlurVal(campo) {
      if (!this.cartao[campo]) {
        this.valFocus[campo] = false;
      }
    },
    onBlurCVV() {
      if (!this.cartao.CVV) {
        this.cvvFocus = false;
      }
    }
  }
};
</script>

<style scoped>
#size_adjust {
  position: fixed;
  top: 50%;
  left: 50%;
  height: 25rem;
  width: 30rem;
  
  transform: translate(-50%, -50%);
}

.popup_content {
  display: flex;
  justify-content: center;
  flex-direction: column;
  gap: 0rem;
}
.main_title {
  text-align: center;
  font-size: 1rem;
  font-weight: bold;
  margin-top: 0.7rem;
  margin-bottom: 0.5rem;
}



.input_group {
  position: relative;
  /* display: flex; */
  /* margin-top: 0.7rem; */
  gap: 0.5rem;
}

.input_payment_popup {
  display: inline-block;
  margin-bottom: 0.7rem;
  padding: 1.3rem 1rem 1.3rem 1rem;
  border-radius: 0.8rem;
  border: 1px solid #dddddd;
  outline: none;
  width: 100%;
  height: 2.7rem;
  box-sizing: border-box;
  font-size: 0.9rem;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  background: white;
}

.input_payment_popup:focus {
  border-color: #d3d3d3;
  box-shadow: #d3d3d3 0px 0px 10px;
}

label {
  position: absolute;
  left: 1rem;
  top: 0.8rem;
  font-size: 0.9rem;
  color: #aaa;
  pointer-events: none;
  transition: all 0.25s ease;
}

label.float {
  top: -0.6rem;
  left: 0.9rem;
  font-size: 0.75rem;
  background: white;
  padding: 0 0.25rem;
  color: #333; /* cor normal ao flutuar */
}

.btn_pagar {
  background-color: #4CAF50;
  width: 100%;
  padding: 1rem 1rem;
  font-weight: 550;
  color: white;
  border: none;
  border-radius: 1rem;
  transition: opacity 0.3s ease;
  margin-bottom: 1rem;
}
.btn_pagar:hover {
  opacity: 90%;
}

.btn_cancel {
  position: absolute;
  top: 1.2rem;
  right: 1.2rem;
  width: 0.7rem;
  height: 0.7rem;
  background-color: transparent;
  border: none;
  cursor: pointer;
  background-image: url('../assets/close.png');
  background-size: contain;
  background-repeat: no-repeat;
  opacity: 70%;
}
.security_img{
  width: 1rem;
  height: 1rem;
  background-image: url('../assets/security.png');
  background-size: contain;
  background-repeat: no-repeat;
  margin-right: 0.5rem;
}
.sub_title {
 
  font-size: 0.8rem;
  color: #4CAF50;
 
}
.security_subtitle {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.2rem;
}

.card_available_img {
  position: absolute;
  left: 0.5rem;
  width: 2rem;
  height: 2rem;
  background-image: url('../assets/vinti4.png');
  background-size: contain;
  background-repeat: no-repeat;
/*   border: 1px solid #dddddd; */
}
</style>

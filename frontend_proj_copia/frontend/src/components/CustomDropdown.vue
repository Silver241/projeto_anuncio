<template>
  <div class="custom-dropdown " @click="toggleDropdown">
    <div class="input_text width_ajust" >{{ selectedLabel }}</div>
    <div v-if="dropdownOpen" class="dropdown-options">
      <div
        class="dropdown-option"
        v-for="option in options"
        :key="option.value"
        @click.stop="selectOption(option)"
      >
        {{ option.label }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    options: Array,
    modelValue: [String, Number, null]
  },
  data() {
    return {
      dropdownOpen: false
    }
  },
  computed: {
    selectedLabel() {
      const found = this.options.find(opt => opt.value === this.modelValue);
      return found ? found.label : 'Escolha uma opção';
    }
  },
  methods: {
    toggleDropdown() {
      this.dropdownOpen = !this.dropdownOpen;
    },
    selectOption(option) {
      this.$emit('update:modelValue', option.value);
      this.dropdownOpen = false;
    },
    handleClickOutside(event) {
      if (!this.$el.contains(event.target)) {
        this.dropdownOpen = false;
      }
    }
  },
  mounted() {
    document.addEventListener('click', this.handleClickOutside);
  },
  beforeUnmount() {
    document.removeEventListener('click', this.handleClickOutside);
  }
}
</script>

<style scoped>
.custom-dropdown {
  position: relative;
  user-select: none;
}
.selected-option {
  border-radius: 0.5rem;
  height: 2rem;
  display: flex;
  align-items: center;
  padding: 0 1rem;
  cursor: pointer;
  border: 1px solid #ccc;
}
.dropdown-options {
  position: absolute;
  top: 110%;
  left: 0;
  width: 100%;
  background: #fff;
  border: 1px solid #ccc;
  border-radius: 0.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  font-size: 0.8rem;
  z-index: 10;
}
.dropdown-option {
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background 0.2s;
}
.dropdown-option:hover {
  background: #e0f7fa;
}
</style>

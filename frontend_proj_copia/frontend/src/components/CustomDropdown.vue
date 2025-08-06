<template>
  <div class="custom-dropdown" ref="dropdown" @click="toggleDropdown">
    <div
      class="input_text width_ajust"
      :class="{ 'placeholder-option': selectedLabel === 'Escolha uma opção' }"
    >
      {{ selectedLabel }}
    </div>

    <transition name="fade-slide">
      <div
        v-if="dropdownOpen"
        class="dropdown-options"
        :style="dropdownStyle"
      >
        <div
          class="dropdown-option"
          v-for="option in options"
          :key="option.value"
          @click.stop="selectOption(option)"
        >
          {{ option.label }}
          <transition name="tooltip-fade">
            <div
              v-if="option.tooltip"
              class="tooltip"
            >
              {{ option.tooltip }}
            </div>
          </transition>
        </div>
      </div>
    </transition>
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
      dropdownOpen: false,
      openUpward: false
    }
  },
  computed: {
    selectedLabel() {
      const found = this.options.find(opt => opt.value === this.modelValue);
      return found ? found.label : 'Escolha uma opção';
    },
    dropdownStyle() {
      return this.openUpward ? { top: 'auto', bottom: '97%' } : {};
    }
  },
  methods: {
    toggleDropdown() {
      this.dropdownOpen = !this.dropdownOpen;
      if (this.dropdownOpen) this.checkDirection();
    },
    selectOption(option) {
      this.$emit('update:modelValue', option.value);
      this.dropdownOpen = false;
    },
    handleClickOutside(event) {
      if (!this.$el.contains(event.target)) {
        this.dropdownOpen = false;
      }
    },
    checkDirection() {
      this.$nextTick(() => {
        const dropdown = this.$refs.dropdown;
        const rect = dropdown.getBoundingClientRect();
        const spaceBelow = window.innerHeight - rect.bottom;
        const spaceAbove = rect.top;
        this.openUpward = spaceBelow < 200 && spaceAbove > spaceBelow;
      });
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

.input_text {
  border: 1px solid #ccc;
  padding: 0.75rem;
  border-radius: 0.75rem;
  cursor: pointer;
  background: white;
  font-size: 0.9rem;
}

.dropdown-options {
  /* padding: 0.06rem; */
  position: absolute;
  top: 110%;
  left: 0;
  width: 100%;
  background: #fff;
  border: 1px solid #ccc;
  border-radius: 0.75rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  font-size: 0.85rem;
  z-index: 10;
}

.dropdown-option {
  position: relative;
  padding: 0.75rem 1rem;
  border-radius: 0.75rem;
  cursor: pointer;
  transition: background 0.3s ease;
}

.dropdown-option:hover {
  background: #e0f7fa;
}

/* Tooltip com animação */
.tooltip {
  opacity: 0;
  pointer-events: none;
  color: #333;
  text-align: left;
  padding: 0.5rem 0.75rem;
  border: 1px solid #ccc;
  border-radius: 0.5rem;
  position: absolute;
  left: 102%;
  top: 50%;
  transform: translateY(-50%);
  white-space: pre-line;
  z-index: 1000;
  width: max-content;
  max-width: 200px;
  background-color: #f9f9f9;
  transition: opacity 0.3s ease;
}

.dropdown-option:hover .tooltip {
  opacity: 1;
  pointer-events: auto;
}

/* Tooltip animation */
.tooltip-fade-enter-active,
.tooltip-fade-leave-active {
  transition: opacity 0.3s ease;
}
.tooltip-fade-enter-from,
.tooltip-fade-leave-to {
  opacity: 0;
}
.tooltip-fade-enter-to,
.tooltip-fade-leave-from {
  opacity: 1;
}

/* Dropdown animation */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.25s ease;
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}
.fade-slide-enter-to {
  opacity: 1;
  transform: translateY(0);
}
.fade-slide-leave-from {
  opacity: 1;
  transform: translateY(0);
}
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);


}

.placeholder-option {
  color: #9f9f9f; /* cinza claro */
}

</style>

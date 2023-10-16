(load-theme 'doom-palenight t)

(map! "C-," #'+workspace:switch-next)

(use-package shr-tag-pre-highlight
  :after shr
  :config
  (add-to-list 'shr-external-rendering-functions
               '(pre . shr-tag-pre-highlight))
  (when (version< emacs-version "26")
    (with-eval-after-load 'eww
      (advice-add 'eww-display-html :around
                  'eww-display-html--override-shr-external-rendering-functions))))


(add-hook! 'rainbow-mode-hook
  (hl-line-mode (if rainbow-mode -1 +1)))

(setq lsp-julia-package-dir nil)

(use-package treesit-auto
  :config
  (global-treesit-auto-mode))

(use-package julia-ts-mode
  :ensure t
  :mode "\\.jl$")

(setq major-mode-remap-alist
      '((julia-mode . julia-ts-mode)))


import mistune

BEGIN = r'\begin{%s}'
END = r'\end{%s}'

enclose = lambda t, s: '\n%s\n%s\n%s\n' % (BEGIN % (t, ), s, END % (t, ))

class LatexRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        return enclose('verbatim', code)

    def block_quote(self, text):
        return enclose('quotation', text)

    def header(self, text, level, raw=None):
        return '\\' + 'sub' * (level - 1) + 'section' + '{%s}\n' % (text)

    def list(self, body, ordered=True):
        return enclose('itemize', body)
        pass

    def list_item(self, text):
        return r'\item ' + text + '\n'


    def paragraph(self, text):
        return text + '\n\n'

    def linebreak(self):
        return '\n'

    def emphasis(self, text):
        return r'\textit{%s}' % (text, )

    def double_emphasis(self, text):
        return r'\textbf{%s}' % (text, )

    def codespan(self, text):
        return r'\texttt{%s}' % (text, )

    def hrule(self):
        return r'\hrulefill'

    def footnotes(self, text):
        print(text)
        return text

    def footnote_ref(self, key, index):
        print(key, index)
        return r'\footnotemark[%s]' % (key, )

    def footnote_item(self, key, text):
        return r'\footnotetext[%s]{%s}' % (key, text)

    def reference(self, key):
        return r'\cite{%s}' % (key, )

    def image(self, src, title, text):
        return '\n'.join([r'\begin{figure}', 
                          r'\includegraphics{%s}' % (src, ), 
                          r'\caption{%s}' % (title, ), 
                          r'\label{%s}' % (text, ), 
                          r'\end{figure}'])

require 'open-uri'
require 'nokogiri'


SITE = 'http://oj.leetcode.com'


def fetch_problem_list
    doc = Nokogiri::HTML(open("#{SITE}/problems/"))

    problems = []
    doc.css('#problemList td a').each do |link|
        problems.push link['href']
    end
    problems
end

def fetch_problem url
    doc = Nokogiri::HTML(open(url))
    desc = doc.css('.question-content').map(&:text).first.strip
    desc = desc.gsub(/\r/, '').gsub(/\n\n/, '\n')
    code = doc.css('#typed_codes textarea[name=typed_code_python]').text
    return desc, code
end

def main
    problems = fetch_problem_list
    problems.each do |problem|
        name = problem.split('/').last
        script = "#{name.gsub(/-/, '_')}.py"
        if !File.exists?(script)
            url = "#{SITE}#{problem}"
            desc, code = fetch_problem url
            content = "#coding: utf-8\n\n'''\n#{url}\n\n#{desc}\n'''\n\n#{code}"
            File.open(script, 'w') { |file| file.write(content) }
        end
    end
end


main

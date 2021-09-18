class MyWorkflow
    def step1
        Digdag.env.store(my_value1:1)
        Digdag.env.store(my_value2:2)
    end

    def step2
        puts "step2: %s" % Digdag.env.params['my_value']
    end

    def step3(my_value1: 0, my_value2: 0)
        puts "my_value1: #{my_value1} my_value2: #{my_value2}"
    end
end